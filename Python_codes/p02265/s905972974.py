from collections import deque

# 命令数入力
n = int(input())
# 命令入力
# order_list = [input().split() for i in range(n)]


# 双方向連結リスト
doubly_linked_list = deque()

for i in range(n):
    
    order = input().split()
    
    if order[0] == "insert":
        doubly_linked_list.appendleft(order[1])
    
    elif order[0] == "delete":
        if order[1] in doubly_linked_list:
            doubly_linked_list.remove(order[1])
    
    elif order[0] =="deleteFirst":
        doubly_linked_list.popleft()
    
    elif order[0] == "deleteLast":
        doubly_linked_list.pop()
        
# 最終結果出力
print(*doubly_linked_list)
