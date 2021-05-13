N = int(input())
print("Three" if len(list(set(map(str,input().split())))) == 3 else "Four")