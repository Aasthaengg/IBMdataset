"""Binary Indexed Tree (Fenwick Tree)"""
class BIT:
    def __init__(self, n):
        self.n = n
        
        #BIT木データ
        self.data = [0]*(n+1)
        
        #元配列
        self.el = [0]*(n+1)
    
    """A1~Aiまでの累積和"""
    def Sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            
            #LSB(Least Significant Bit)の獲得:i&(-i)
            i -= i & (-i) 
        return s
    
    """Ai += x"""
    def Add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    """Ai ~ Ajまでの累積和"""
    def Get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.Sum(j) - self.Sum(i)
    
s = input()
s = s.replace('BC', 'D')
mode = 0
res = 0
for i in range(len(s)):
    if s[i] == 'B' or s[i]=='C':
        mode = 0
    elif s[i] == 'A':
        mode += 1
    else:
        res += mode
print(res)