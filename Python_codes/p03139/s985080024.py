N,A,B = map(int, input().split())
#質問 1 に対して「はい」と回答した人の数は A 人、質問 2 に対して「はい」と回答した人の数は B人でした。
#このとき、調査の対象者のうち新聞 X, Y の両方を購読している人の数は最大で何人であり、また最小で何人であると考えられるでしょうか？
if N-A-B >= 0:
    print(min(A,B),0)
else:
    print(min(A,B),abs(N-A-B))