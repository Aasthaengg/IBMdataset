def main():
    from collections import deque

    N, M = map(int, input().split())
    connected_rooms = [[] for i in range(N + 1)]
    
    for i in range(M):
        a, b = map(int, input().split())
        connected_rooms[a].append(b)
        connected_rooms[b].append(a)
    
    def Breadth_First_Search(root):
        queue = deque([root]) #calculate distance from the root
        distance = [None] * (N + 1) #initialize distance
        distance[root] = 0
        
        while (queue): #do BFS and calculate distance recursively
            ver = queue.popleft()
            
            for index in connected_rooms[ver]:
                if (distance[index] == None):
                    distance[index] = distance[ver] + 1
                    queue.append(i)
        
        return (distance)
    
    dist = [None] * (N + 1)
    dist[0] = True
    
    Q = deque([1])
    while (Q):
        index = Q.popleft()
        for j in connected_rooms[index]:
            if (dist[j] == None):
                dist[j] = index
                Q.append(j)
    
    if (all(dist)):
        print('Yes')
        for i in dist[2:]:
            print(i)
    else:
        print('No')


if __name__ == '__main__':
    main()