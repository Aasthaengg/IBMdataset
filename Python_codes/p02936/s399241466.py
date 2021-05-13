from collections import deque

def main():
    n, q = list(map(int, input().split(" ")))
    v_list = [[] for i in range(n)]
    for _ in range(n-1):
        a, b = list(map(int, input().split(" ")))
        v_list[a-1].append(b-1)
        v_list[b-1].append(a-1)

    p_x_list = [0]*n
    for _ in range(q):
        p, x = list(map(int, input().split(" ")))
        p_x_list[p-1]+=x

    point_list = [0]*n
    checked_list = [0]*n
    stack = deque([0]) 
    while stack:
        cur = stack.pop()
        checked_list[cur] = 1
        point_list[cur]+=p_x_list[cur]
        for next_i in v_list[cur]:
            if checked_list[next_i]:
                continue
            stack.append(next_i)
            point_list[next_i]+=point_list[cur]
   
    print(*point_list)

if __name__=="__main__":
    main()
