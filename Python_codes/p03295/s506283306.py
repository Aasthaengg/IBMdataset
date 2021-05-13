from sys import stdin
input = stdin.buffer.readline

def main():
    n, m = map(int, input().split())
    
    ab = [0] * m
    for ind in range(m):
        i, j = map(int, input().split())
        ab[ind] = (i-1, j-1)
    
    ab.sort()

    ans = 1
    right = ab[0][1]
    for ind in range(1, m):
        # ab[ind] ∩ a[ind-1] = Φ
        if right <= ab[ind][0]:
            ans += 1
            right = ab[ind][1]

        # ab[ind] ⊆ ab[ind-1]
        elif ab[ind][1] < right:
                right = ab[ind][1]
        
        # else:
            # pass
    
    print(ans)

main()