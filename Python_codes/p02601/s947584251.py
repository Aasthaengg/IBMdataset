import sys
input = sys.stdin.readline  #文字列では使わない
A,B,C = map(int, input().split())
K = int(input())
count =0
while A >=B:
    B *=2
    count +=1

while B >=C:
    C *=2
    count +=1

if A < B < C and count <=K:
    print("Yes")
else:
    print("No")