N = int(input())
students = list(map(int, input().split()))

sorted_students = [str(x[0] + 1) for x in sorted([x for x in enumerate(students)], key=lambda x: x[1])]

print(' '.join(sorted_students))