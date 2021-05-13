def solve():
    N = int(input())
    word_count = {}
    max_count = 0
    for i in range(N):
        word = input()
        word_count[word] = word_count.get(word, 0) + 1
        max_count = max(word_count[word], max_count)
    ans_words = []
    for w,c in word_count.items():
        if c == max_count:
            ans_words.append(w)
    print('\n'.join(sorted(ans_words)))

if __name__ == "__main__":
    solve()