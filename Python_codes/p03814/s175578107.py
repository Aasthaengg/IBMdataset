import sys
input = sys.stdin.readline

S = input().rstrip('\n')
print(S.rfind("Z") - S.find("A") + 1)
