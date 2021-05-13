m=int(input())//2
l=sorted(map(int,input().split()))
print(l[m]-l[~m])