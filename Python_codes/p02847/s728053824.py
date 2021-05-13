import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

s = input()
d = {"SUN": 7, "MON": 6, "TUE": 5,"WED": 4, "THU": 3,"FRI":2,"SAT":1}
print(d[s])