s = input()
n = int(input())

i = 0
while i*n < len(s):
    print(s[i*n],end = "")
    i +=1