n = int(input())
a = input()
b = input()
ans = ''
idx1 = 0
idx2 = n
while idx1 < n and a[idx1:] != b[:idx2]:
    idx1+=1
    idx2-=1
print(2*n - idx2)