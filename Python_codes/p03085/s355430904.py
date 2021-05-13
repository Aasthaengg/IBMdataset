import sys

b = sys.stdin.readline().strip()
dic = {"A": "T", "T": "A", "C": "G", "G": "C"}
print(dic[b])