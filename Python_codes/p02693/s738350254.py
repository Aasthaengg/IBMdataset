K = int(input())
count = 0
number = K
A, B = map(int, input().split())
while number < A:
    count += 1
    number = K * count

if number <= B:
    print("OK")
else:
    print("NG")