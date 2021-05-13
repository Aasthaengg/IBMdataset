def main():
    from collections import Counter
    from heapq import heapify,heappop,heappush
    H,W = map(int,input().split())
    A = ''
    for i in range(H):
        A += input()
    A = list(A)
    num_chars = list(map(lambda x: -x, Counter(A).values()))
    heapify(num_chars)
    # H == 1 or W == 1

    for i in range((H//2)*(W//2)):
        num = heappop(num_chars)
        
        if -4 < num:
            print('No')
            return
        else:
            heappush(num_chars,num+4)

    if H & 1:
        for i in range(W//2):
            num = heappop(num_chars)
            if -2 < num:
                print('No')
                return
            else:
                heappush(num_chars,num+2)

    if W & 1:
        for i in range(H//2):
            num = heappop(num_chars)
            if -2 < num:
                print('No')
                return
            else:
                heappush(num_chars,num+2)


    if H & 1 and W & 1:
        if num_chars[0] != -1:
            return
    print('Yes')
    return
    






main()