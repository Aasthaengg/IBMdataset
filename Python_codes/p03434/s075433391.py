N = int(input())
li = list(map(int,input().split()))
li.sort()
li = li[::-1]

Alice = li[0::2]
Bob = li[1::2]

print(sum(Alice)-sum(Bob))