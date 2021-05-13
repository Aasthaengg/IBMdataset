from heapq import heapify, heappop, heappush
N,H = map(int,input().split())
HQ = []
for i in range(N):
  a,b = map(int,input().split())
  heappush(HQ,(-a,0)) #IDとして0なら何度でも使える
  heappush(HQ,(-b,1))
ans = 0
prev_damage = -1
prev_id = -1
while H > 0:
  damage, ID = heappop(HQ); damage *= -1 #ダメージを正に
  if damage == prev_damage and prev_id == 0 and prev_id == ID:
    nokori = (H+damage-1)//damage
    ans += nokori
    print(ans)
    exit()
  H -= damage
  ans += 1
  prev_damage = damage; prev_id = ID
  if ID == 0:
    heappush(HQ,(-damage, ID))
print(ans)
