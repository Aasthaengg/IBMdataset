n = int(raw_input())
S = map(int, raw_input().split())
q = int(raw_input())
T = map(int, raw_input().split())

x = set(S) & set(T)
print len(x)