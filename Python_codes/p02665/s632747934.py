import math

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_at_level = [0]*(N+1)
    total_leafs = sum(A)
    large_level = math.ceil(math.log(total_leafs, 2))
    vertices_in_layer = 1
    total_vertex_count = 0
    next_level_possible_space = 1
    for level in range(N+1):
        level_possible_space = next_level_possible_space
        leafs_in_level = A[level]
        total_leafs -= leafs_in_level
        # print(f"total_leafs: {total_leafs}, leafs_in_level: {leafs_in_level}, level_possible_space: {level_possible_space}")
        level_open_space = level_possible_space - leafs_in_level
        if level_open_space < 0:
            print(-1)
            return
        additional_vertices_in_level = min(level_open_space, total_leafs)
        total_vertex_count += leafs_in_level + additional_vertices_in_level
        next_level_possible_space = min(2*level_open_space, total_leafs)

    print(total_vertex_count)

if __name__ == '__main__':
    main()
