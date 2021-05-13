def main():
    K,S  = map(int,(input().split()))
    cnt = 0

    for X in range(K+1):
        for Y in range(K+1):
            Z = S - X - Y
            if 0 <= Z and Z<=K :
                cnt+=1
    
    print(cnt)






if __name__ == '__main__':
    main()
