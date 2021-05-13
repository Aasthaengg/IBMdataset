num = list(map(int, input().split()))
k = int(input())
k = 2**k
tmp = sorted(num)

print(tmp[0]+tmp[1]+tmp[2]*k)