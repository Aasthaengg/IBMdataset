def solve():
    A,B,C,D = [int(i) for i in input().split()]
    takahashi_attack_cnt = (C+B-1) // B
    aoki_attack_cnt = (A+D-1) // D
    if takahashi_attack_cnt <= aoki_attack_cnt:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()