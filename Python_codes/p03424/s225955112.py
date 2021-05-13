n = int(input())
s = list(input().split())
hina = set(s)
arare = len(hina)
if arare == 3:
    print("Three")
else:
    print("Four")