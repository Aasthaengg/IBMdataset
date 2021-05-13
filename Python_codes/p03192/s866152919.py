N=int(input())
lst = []
while N > 0:
    lst.append(N%10)
    N //= 10 # 必須
lst.reverse()
print(lst.count(2))
