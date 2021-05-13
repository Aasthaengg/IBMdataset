"""
Given N, D, A, N means no. of monsters, D means distances of bombs, A attack of the bombs

Find the minimum of bombs required to win.

Each monster out of N pairs - pair[0] = position, pair[1] = health

hashmap[i] = H

pref

"""
from collections import deque

mod = 1e9+7
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    INF = 1e9 + 7
    N, D, A = [int(x) for x in raw_input().split()]
    D *= 2
    monsters = []
    #m = {}
    change = [0 for _ in range(N)]
    for _ in range(N):
        pos, health = [int(x) for x in raw_input().split()]
        #m[pos] = m.get(pos, 0) + health
        #smallest_x = min(smallest_x, pos)
        #biggest_x = max(biggest_x, pos)
        health = (health + A - 1) // A
        #print(health)
        
        monsters.append([pos, health])    
    """
    remain_attack = 0
    ans = 0
    for cur in range(smallest_x, biggest_x+1):
        if cur in m and m[cur] > remain_attack:
            remained_health = m[cur] - remain_attack
            times = remained_health / A if remained_health % A == 0 else remained_health // A + 1
            attack = times * A
            pref_sum[cur + D] = pref_sum.get(cur + D, 0) - attack
            remain_attack += attack
            ans += times
        remain_attack += pref_sum.get(cur, 0)
            
    """   
            
    monsters.sort(key = lambda x : x[0])
    
    #remain_attacks_queue = deque([])
    
    #remain_attack = 0
    running_sum = 0
    
    ans = 0
    
    for i in range(N):
        pos, health = monsters[i]
        running_sum += change[i]
        #print(health, running_sum)
        my_health = health - running_sum
        if my_health <= 0:
            continue # Already killed
        
        # Find the last monster hit by this range
        lo = i+1
        hi = N-1
        ok = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            #print(mid, monsters[mid])
            if monsters[mid][0] <= pos + D:
                ok = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        if ok != -1:
            running_sum += my_health
        if ok + 1 < N:
            change[ok+1] -= my_health
            
            
        ans += my_health
        
                
        """
        while len(remain_attacks_queue) and monster[0] - D > remain_attacks_queue[0][0]:
            remain_attack -= remain_attacks_queue.popleft()[1]
        if remain_attack < monster[1]:
            remained_health = monster[1] - remain_attack
            times = remained_health / A if remained_health % A == 0 else remained_health // A + 1
            #print(times)
            attack = times * A
            remain_attacks_queue.append([monster[0], attack])
            ans += times
            remain_attack += attack
        """
    
        
    print(ans)
    

main()