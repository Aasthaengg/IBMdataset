n = int(input())
l = sorted(list(map(int,input().split(' '))))

print(l[int(n/2)] - l[int(n/2)-1])