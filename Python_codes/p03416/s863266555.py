s = input().split()
a = int(s[0])
b = int(s[1])

def palindromic(x):
    y = list(x)
    if not y[0] == y.pop():
        return False
    if not y[1] == y.pop():
        return False
    return True

answer = 0

for i in range(a, b + 1):
    if palindromic(str(i)):
        answer += 1
    
print(answer)