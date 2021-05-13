from collections import defaultdict

def main():
    N, M = map(int, input().split())
    a = [input().split() for _ in range(M)]
    ac_count = [0] * (N + 1)
    wa_count = defaultdict(lambda:0)
    ac, wa = 0, 0

    for q_no, ans in a:
        q_no = int(q_no)
        if ac_count[q_no] == 0:
            if ans == "AC":
                ac_count[q_no] = 1
                ac += 1
                wa += wa_count.get(q_no, 0)
            else:
                wa_count[q_no] += 1
    
    print(ac, wa)

if __name__ == '__main__':
    main()