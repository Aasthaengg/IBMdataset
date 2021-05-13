N = int(input())
A, B = map(int,input().split())
P = list(map(int,input().split()))

P.sort()
d = {
    "A":0,
    "B":0,
    "C":0,
}
for p in P:
    if p <= A:
        d["A"] += 1
    elif p <= B:
        d["B"] += 1
    else:
        d["C"] += 1

print(min(d["A"],d["B"],d["C"]))
