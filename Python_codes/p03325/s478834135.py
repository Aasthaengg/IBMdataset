n = int(input())
A = list(map(int,input().split()))
ans = sum((a & -a).bit_length() - 1 for a in A)
print(ans)
