cards = [[0 for i in range(13)] for j in range(4)]

pattern = ["S", "H", "C", "D"]

n = int(input())

ch_list=[]
rank_list_0=[]
while n > 0:
  ch, rank = input().split()
  ch_list.append(ch)
  rank_list_0.append(rank)
  n = n - 1

rank_list = [int(rank_list) for rank_list in rank_list_0]

for (chlist, ranklist) in zip(ch_list,rank_list):
      cards[pattern.index(chlist)][ranklist-1] = 1
      
for i in range(0, 4):
  for j in range(0, 13):
    if cards[i][j] == 0:
        print(pattern[i], j+1)
