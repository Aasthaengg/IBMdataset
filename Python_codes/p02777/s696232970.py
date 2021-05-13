s, t = input().split()
a, b = map(int, input().split())
u = input()

countdict = {}
countdict[s] = a
countdict[t] = b
countdict[u] -= 1

print(str(countdict[s]) + " " + str(countdict[t]))