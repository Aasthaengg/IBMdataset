def solution(s):
  return s + 'es' if s[-1] == 's' else s + 's'
print(solution(input()))