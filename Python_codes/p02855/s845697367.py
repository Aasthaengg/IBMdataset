def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()

    H,W,K = map(int,input().split())
    map_input = [list(input()) for _ in range(H)]

    #solve
    ans = [[-1]*W for i in range(H)]
    queue = []
    strawberry_idx = 0
    
    for i in range(H):
        strawberry_idx+=1
        flag = True
        if all(j=='.' for j in map_input[i]):
            strawberry_idx-=1
            queue.append(i)
            continue
        else:
            for j in range(W):
                if map_input[i][j]=='#':
                    if flag:
                        flag = False
                    else:
                        strawberry_idx+=1
                ans[i][j] = strawberry_idx
            if queue:
                for q in queue:
                    ans[q] = ans[i]
                queue = []
    if queue:
        for q in queue:
            ans[q] = ans[min(queue)-1]
    for a in ans:
        print(*a) 

if __name__=='__main__':
    main()