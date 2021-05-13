import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))

    surplus_scores = []
    sum_lack_score = 0
    ans = 0
    for a, b in zip(A, B):
        if a > b:
            surplus_scores.append(a - b)
        elif a < b:
            sum_lack_score += b - a
            ans += 1

    if sum_lack_score > 0:
        surplus_scores.sort(reverse=True)
        pass_exam = False
        for i, score in enumerate(surplus_scores):
            sum_lack_score -= score
            if sum_lack_score <= 0:
                ans += (i + 1)
                pass_exam = True
                break
        if not pass_exam:
            ans = -1

    print(ans)


if __name__ == "__main__":
    main()
