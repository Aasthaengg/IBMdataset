from collections import Counter
s = input()
ac = [0]

def power_func(a,b,p):
    """a^b mod p を求める"""
    if b==0: return 1
    if b%2==0:
        d=power_func(a,b//2,p)
        return d*d %p
    if b%2==1:
        return (a*power_func(a,b-1,p ))%p

for i in range(len(s)):
    char = s[i]
    digit = len(s) - i - 1
    ac.append((ac[-1] + (int(char) * power_func(10, digit, 2019))) % 2019)
#print(ac)

C = Counter(ac)
#print(C)
ans = 0
for val in C.values():
    ans += val * (val - 1) // 2
print(ans)