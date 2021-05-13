def main():
    import math

    N = int(input())
    
    ans_list = [0 for i in range(N)]
    
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):

                left_eq = x * x + y * y + z * z + x * y + y * z + z * x
                if (left_eq <= N):
                    ans_list[left_eq - 1] += 1
    
    for i in range(N):
        print(ans_list[i])

if __name__ == '__main__':
    main()
