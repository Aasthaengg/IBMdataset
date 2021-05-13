#data = map(int,input().split())
data = [int(input()),int(input())]

if data[0] % 500 <= data[1]:
    print("Yes")
else:
    print("No")