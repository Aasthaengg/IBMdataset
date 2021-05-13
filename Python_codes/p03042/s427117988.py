#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

s = input()

temp1 = int(s[0:2])
temp2 = int(s[2:4])

if temp1 >= 1 and temp1 <= 12:
    if (temp2 < 1 or temp2 > 12):
        print("MMYY")
    else:
        print("AMBIGUOUS")
else:
    if (temp2 >= 1 and temp2 <= 12):
        print("YYMM")
    else:
        print("NA")
