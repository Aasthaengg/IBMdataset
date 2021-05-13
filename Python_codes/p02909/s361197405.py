
def f(s):
	es = ['Sunny', 'Cloudy', 'Rainy']
	h = {e:i for i,e in enumerate(es)}
	return es[(h[s] + 1)%3]

print f(raw_input())