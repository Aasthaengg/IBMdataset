n = int(input())

al = list(input().split())

for i in range(n):
    if al[i] =="Y":
        print("Four")
        exit()

print("Three")