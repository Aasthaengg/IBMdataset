n = int(input())
a, b = map(int, input().split())
score = list(map(int, input().split()))

one = len([i for i in score if i <= a])
two = len([i for i in score if (a < i <= b)])
three = n - one - two
print(min((one, two, three)))