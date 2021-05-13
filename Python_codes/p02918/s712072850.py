n_k = list(map(int,input().split()))
chr_lr = list(input())
cnt_rl = 0
cnt_con = 0

for i in range(n_k[0]-1):
  if(chr_lr[i] == chr_lr[i+1]):
    cnt_con += 1

sum = min(cnt_con + 2*n_k[1],n_k[0]-1)
print(sum)