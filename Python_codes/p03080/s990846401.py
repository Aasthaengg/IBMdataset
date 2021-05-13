n=int(input())
s=input()
print("YNeos"[s.count('R')<=s.count('B')::2])