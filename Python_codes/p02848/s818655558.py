N = int(input())
S = input()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in S:
    print(abc[(abc.index(i)+N)%len(abc)], end = "")