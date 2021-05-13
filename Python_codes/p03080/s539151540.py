import collections
input()
c=collections.Counter(input())
print("YNeos"[c["R"]<=c["B"]::2])