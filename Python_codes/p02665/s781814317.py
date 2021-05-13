def main():
    N = int(input())
    A = list(map(int, input().split()))
    all_leave_num = sum(A)

    if((len(A) != 1 and A[0] != 0) or (len(A) == 1 and A[0] != 1)):
        print(-1)
        return

    # Init
    node_num = 0
    next_node_w_children = 1
    next_node_num = 1
    
    for i in range(N+1):
        node_in_the_dept = next_node_num
        node_w_children = next_node_w_children      

        if(i == N):
            node_num += node_in_the_dept
            print(node_num)
        else:
            next_leaf_num = A[i+1]
            all_leave_num -=A[i]

            next_node_num = min(2 * node_w_children, all_leave_num)
            next_node_w_children = next_node_num - next_leaf_num
            if(next_node_num > node_w_children * 2 or next_node_num < node_w_children or next_node_w_children < 0):
                print(-1)
                return
            node_num += node_in_the_dept
    

main()