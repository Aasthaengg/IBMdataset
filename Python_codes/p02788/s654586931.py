import bisect
import itertools
import sys

input=sys.stdin.readline

def main(args):
    n, d, a = map(int,input().split())
    
    monster = [0]*n
    pos = [0]*n
    for i in range(n):
        x, h = map(int,input().split())
        monster[i] = (x, -(-h//a))
        pos[i] = x
    
    pos.sort()
    monster.sort()
    
    limit = [0]*n
    #そのモンスターを攻撃したとき巻き添えにできるやつらの中で一番右のヤツのindex
    for i in range(n):
        limit[i] = bisect.bisect_right(pos, pos[i]+2*d)-1
    
    #print(limit)
    
    damage = [0]*(n+1)
    ans = 0
    for i in range(n):
        if damage[i] >= monster[i][1]:
            pass
        else:
            plus = monster[i][1] - damage[i]
            ans += plus
            damage[i] += plus
            damage[limit[i]+1] -= plus
        #print(damage)
        
        damage[i+1] += damage[i]
    
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])