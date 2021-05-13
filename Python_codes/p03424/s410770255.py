n = input()
l = list(map(str,input().split()))
print("Four" if len(set(l)) == 4 else "Three")