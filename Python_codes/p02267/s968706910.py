S_num = int(input())
seq_S = set(input().split(" "))
T_num = int(input())
seq_T = set(input().split(" "))

seq_Both = seq_S & seq_T

print(len(seq_Both))