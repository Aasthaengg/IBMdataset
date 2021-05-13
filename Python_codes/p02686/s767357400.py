# Hello from https://codeforces.com/gym/101341/problem/A

class BracketString:
    def __init__(self, s, i):
        self.i = i
 
        balance = 0
        minimum = 0
        for c in s:
            if c == "(":
                balance += 1
            else:
                balance -= 1
                minimum = min(minimum, balance)
 
        revBalance = 0
        revMinimum = 0
        for c in reversed(s):
            if c == ")":
                revBalance += 1
            else:
                revBalance -= 1
                revMinimum = min(revMinimum, revBalance)
 
        assert balance == -revBalance
 
        self.balance = balance
        self.minimum = minimum
        self.revMinimum = revMinimum
 
    @staticmethod
    def cmpForPositive(a, b):
        return b.minimum - a.minimum
 
    @staticmethod
    def cmpForNegative(a, b):
        return a.revMinimum - b.revMinimum
 
 
n = int(raw_input())
positive = []
negative = []
neutral = []
sumBalance = 0
for i in xrange(n):
    s = raw_input()
    bs = BracketString(s, i)
    if bs.balance > 0:
        positive.append(bs)
    elif bs.balance < 0:
        negative.append(bs)
    else:
        neutral.append(bs)
    sumBalance += bs.balance
 
if sumBalance != 0:
    print "No"
    exit()
 
positive.sort(cmp=BracketString.cmpForPositive)
negative.sort(cmp=BracketString.cmpForNegative)
 
ans = []
curBalance = 0
 
for bs in positive + neutral + negative:
    if curBalance + bs.minimum < 0:
        print "No"
        exit()
    curBalance += bs.balance
    ans.append(bs.i + 1)
 
print "Yes"
